# Investigating Necessity and Sufficiency of Multimodal Interaction in Music-QA LLMs via audioDIME

<!-- TODO: arXiv badge once available, e.g.
[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/XXXX.XXXXX)
-->
*Author list — TODO*

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

<!-- TODO: short tree + one-line description per folder, e.g.

QA_analysis/
├── utils/            core audioDIME/LIME implementation
├── experiments/       Exp A (ranking) / Exp E (perturbations) base scripts
├── paper/              Qwen2.5-Omni experiments (3 conditions)
├── paper_af3/          Audio Flamingo 3 experiments (3 conditions)
└── assets/             images used in this README
-->

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

<!-- TODO:
- HumMusQA: where to get it, expected directory layout (parquet files)
- any precomputed cache needed (e.g. demucs stem-separation cache) and how
  to (re)generate it
-->

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
