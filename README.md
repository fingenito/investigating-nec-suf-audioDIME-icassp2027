# Investigating Necessity and Sufficiency of Multimodal Interaction in Music-QA LLMs via audioDIME

<!-- TODO: arXiv badge once available, e.g.
[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/XXXX.XXXXX)
-->
arXiv still not available!

*Flavio Ingenito, Luca Comanducci, Francesca Ronchini, Paolo Bestagini*

<p align="center">
  <img src="./assets/audioDIMEpipe_w.png" width="80%"/>
</p>

This repository contains the code for *[Investigating Necessity and Sufficiency of
Multimodal Interaction in Music-QA LLMs via audioDIME]()*, submitted to ICASSP 2027.

<!-- TODO: one paragraph, plain language, no equations:
- what question the paper asks (does the model really need both audio and text,
  or is it guessing from one modality alone?)
- which models: Qwen2.5-Omni and Audio Flamingo 3
- which dataset/task: HumMusQA, 4-option music question answering
- one-sentence description of audioDIME as the tool used to answer it
-->

In this paper, we investigate how Large Audio Language Models (LALM) combine input modalities, audio and text, to generate a response. To do this, we propose audioDIME, an adaptation of the [DIME](https://arxiv.org/pdf/2203.02013) framework to the audio-musical domain, to disentangle unimodal contributions from multimodal interactions in [Qwen2.5-Omni-7B](https://arxiv.org/pdf/2503.20215) and [AudioFlamingo3](https://arxiv.org/pdf/2507.08128) on [HumMusQA](https://arxiv.org/pdf/2603.27877), and evaluate their necessity and sufficiency through masking.

## Method

<!-- TODO: short explanation (no more than mamba-foley's own level of detail):
- audioDIME in one paragraph: decomposes the model's answer into a unimodal
  contribution per modality (UC_audio, UC_text) plus a multimodal interaction
  term (MI), via LIME surrogates over audio segments / question words
- necessity & sufficiency in one paragraph: progressively masking the top-k
  ranked features and re-scoring the 4-option answer
- the three conditions: complete / audio_only / text_only
-->

<!-- TODO: second figure, e.g. qwen_suf_nec_combined_row (necessity+sufficiency
     curves for one model, three conditions side by side) -->
<p align="center">
  <img src="./assets/results_overview.png" width="90%"/>
</p>

## Repository structure

The repository is organised as follows:
* `QA_analysis/utils` — the core audioDIME implementation: audio segmentation, masking, LIME surrogate fitting, and the GPU runners used to query the models.
* `QA_analysis/experiments` — base scripts shared across all experiments: building the audioDIME ranking (Exp A) and running the masking-based perturbations used to compute necessity and sufficiency (Exp E).
* `QA_analysis/paper` — experiments run on Qwen2.5-Omni, one subfolder per condition (complete, audio-only, text-only).
* `QA_analysis/paper_af3` — the same three experiments run on Audio Flamingo 3.

## Setup

<!-- TODO, mirroring mamba-foley's Setup section:
1. git clone
2. conda/venv env creation
3. install torch/torchaudio/torchvision with the correct CUDA index (see
   requirements.txt header)
4. pip install -r requirements.txt
5. note: transformers version differs for Qwen vs Audio Flamingo 3 (see
   requirements.txt comments)
-->

## Dataset

We use [HumMusQA](https://arxiv.org/pdf/2603.27877), a benchmark of 320 expert-written, multiple-choice music questions (4 options each) paired with Creative-Commons-licensed audio from Jamendo. Questions were authored and validated by music theory experts specifically to require genuine listening, rather than being auto-generated from captions/tags — a known failure mode of prior music-QA datasets, which are often solvable by text-only models exploiting language priors alone. This makes HumMusQA particularly well-suited to our study: probing whether models actually need the audio, or can shortcut through text, is precisely the question our necessity/sufficiency analysis addresses. Questions span 13 musical categories (e.g. melody, harmony, instrumentation, cultural context) and 3 difficulty levels.

## Running the experiments

<!-- TODO, replaces mamba-foley's Inference/Training sections:
### Exp A — building the audioDIME ranking
  command(s) to run batch_exp_a.py for a given model/condition
### Exp E — necessity & sufficiency curves
  command(s) to run batch_exp_e.py, pointing --exp-a-dir at Exp A's output
- table or list of the 6 (model x condition) combinations
-->

## Results

<!-- TODO: 2-3 bullet points on the main findings, pointing to the figures in
     assets/; link to the paper once available -->

## Citation

<!-- TODO: bibtex, once the paper has a public entry (arXiv/ICASSP proceedings) -->
```bibtex

```

## License

<!-- TODO: not decided yet -->
