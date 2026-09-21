---
layout: default
title: "Investigating Necessity and Sufficiency of Multimodal Interaction in Music-QA LLMs via audioDIME"
---

Accompanying website to the paper _Investigating Necessity and Sufficiency of Multimodal Interaction in Music-QA LLMs via audioDIME_, submitted to ICASSP 2027.

## Abstract

Audio LLMs have advanced music understanding, yet how they combine audio and text remains unclear, and standard attribution cannot distinguish correlation from causal reliance. We adapt DIME to disentangle unimodal contributions from multimodal interactions in Qwen2.5-Omni-7B and AudioFlamingo3 on HumMusQA, and evaluate their necessity and sufficiency through masking. Across both models, audio's unimodal contribution is often sufficient but rarely necessary, whereas interaction features have substantially higher necessity and, under complete input, approach text contributions. These results suggest that audio primarily influences predictions through its interaction with the question rather than as an independent decision signal.

## Additional material

### Sufficiency & Necessity of MI

For each sample, sufficiency measures whether the top-ranked MI (multimodal interaction) features alone preserve the model's confidence in its original answer, while necessity measures whether removing them destroys that confidence, both normalized against chance level. Results are reported separately for samples where the model's original prediction was correct or incorrect.

- Qwen2.5-Omni, complete condition
<p align="center">
  <img src="assets/img/qwen_complete_mi_by_correctness.png" width="55%"/>
  <br/>
  <em>Qwen2.5-Omni — complete condition.</em>
</p>

- Qwen2.5-Omni, audio-only condition
<p align="center">
  <img src="assets/img/qwen_audio_only_mi_by_correctness.png" width="55%"/>
  <br/>
  <em>Qwen2.5-Omni — audio-only condition.</em>
</p>

- Qwen2.5-Omni, text-only condition
<p align="center">
  <img src="assets/img/qwen_text_only_mi_by_correctness.png" width="55%"/>
  <br/>
  <em>Qwen2.5-Omni — text-only condition.</em>
</p>

- Audio Flamingo 3, complete condition
<p align="center">
  <img src="assets/img/af3_complete_mi_by_correctness.png" width="55%"/>
  <br/>
  <em>Audio Flamingo 3 — complete condition.</em>
</p>

- Audio Flamingo 3, audio-only condition
<p align="center">
  <img src="assets/img/af3_audio_only_mi_by_correctness.png" width="55%"/>
  <br/>
  <em>Audio Flamingo 3 — audio-only condition.</em>
</p>

- Audio Flamingo 3, text-only condition
<p align="center">
  <img src="assets/img/af3_text_only_mi_by_correctness.png" width="55%"/>
  <br/>
  <em>Audio Flamingo 3 — text-only condition.</em>
</p>
