---
layout: default
title: "Investigating Necessity and Sufficiency of Multimodal Interaction in Music-QA LLMs via audioDIME"
---

Accompanying website to the paper _Investigating Necessity and Sufficiency of Multimodal Interaction in Music-QA LLMs via audioDIME_, submitted to ICASSP 2027.

## Abstract

Audio LLMs have advanced music understanding, yet how they combine audio and text remains unclear, and standard attribution cannot distinguish correlation from causal reliance. We adapt DIME to disentangle unimodal contributions from multimodal interactions in Qwen2.5-Omni-7B and AudioFlamingo3 on HumMusQA, and evaluate their necessity and sufficiency through masking. Across both models, audio's unimodal contribution is often sufficient but rarely necessary, whereas interaction features have substantially higher necessity and, under complete input, approach text contributions. These results suggest that audio primarily influences predictions through its interaction with the question rather than as an independent decision signal.

## Additional material

### <!-- TODO -->

<p align="center">
  <img src="assets/img/qwen_audio_only_mi_by_correctness.png" width="90%"/>
</p>

<p align="center">
  <img src="assets/img/qwen_text_only_mi_by_correctness.png" width="90%"/>
</p>

<p align="center">
  <img src="assets/img/af3_audio_only_mi_by_correctness.png" width="90%"/>
</p>

<p align="center">
  <img src="assets/img/af3_text_only_mi_by_correctness.png" width="90%"/>
</p>
