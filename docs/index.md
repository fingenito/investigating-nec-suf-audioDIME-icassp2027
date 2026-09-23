---
layout: default
title: "Investigating Necessity and Sufficiency of Multimodal Interaction in Music-QA LLMs via audioDIME"
---

Accompanying website to the paper _Investigating Necessity and Sufficiency of Multimodal Interaction in Music-QA LLMs via audioDIME_, by _Flavio Ingenito, Luca Comanducci, Francesca Ronchini, Paolo Bestagini_, submitted to ICASSP 2027.

## Abstract

Audio LLMs have advanced music understanding, yet how they combine audio and text remains unclear, and %standard attribution cannot distinguish correlation from causal reliance
standard attribution methods do not test whether attributed features are necessary or sufficient under intervention. We adapt DIME to disentangle unimodal contributions from multimodal interactions in Qwen2.5-Omni-7B and AudioFlamingo3 on HumMusQA, and evaluate their necessity and sufficiency through masking. Across both models, audio’s unimodal contribution is often sufficient but rarely necessary, whereas interaction features have substantially higher necessity and, under complete input, approach text contributions. These results suggest that audio primarily influences predictions through its interaction with the question rather than as an independent decision signal.

## Additional Material

Due to space constraints, the paper reports sufficiency and necessity results only for the complete condition of both models. Here, we provide the extended results for all conditions, together with a worked example that verifies the audio segmentation. Specifically, we present:

- Sufficiency and necessity of `MI`, split by prediction correctness, for all six combinations of model (Qwen2.5-Omni and AudioFlamingo3) and condition (complete, audio-only, and text-only).
- The same breakdown for `UC_text`, `UC_audio`, and `MI` (modality diagnosis), considering correct predictions only, again for all six combinations.
- A worked example of onset-guided audio segmentation for one HumMusQA sample, showing that the resulting segments are meaningful and correctly localized in time.

Samples with <em>p<sub>orig</sub></em> &lt; 0.40 are excluded from every curve, as the normalization denominator would otherwise be too small and unstable. The table below reports, out of 320 samples, how many remain after this filter for each model and condition, split according to whether the model's original prediction was correct. This makes the effective sample size behind each curve explicit.

<table align="center">
  <thead>
    <tr>
      <th align="left">Model</th>
      <th align="left">Condition</th>
      <th align="right">Remaining</th>
      <th align="right">Correct</th>
      <th align="right">Incorrect</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Qwen2.5-Omni</td><td>Complete</td><td align="right">300</td><td align="right">192</td><td align="right">108</td></tr>
    <tr><td>Qwen2.5-Omni</td><td>Audio-only</td><td align="right">270</td><td align="right">120</td><td align="right">150</td></tr>
    <tr><td>Qwen2.5-Omni</td><td>Text-only</td><td align="right">283</td><td align="right">100</td><td align="right">183</td></tr>
    <tr><td>AudioFlamingo3</td><td>Complete</td><td align="right">300</td><td align="right">204</td><td align="right">96</td></tr>
    <tr><td>AudioFlamingo3</td><td>Audio-only</td><td align="right">283</td><td align="right">175</td><td align="right">108</td></tr>
    <tr><td>AudioFlamingo3</td><td>Text-only</td><td align="right">290</td><td align="right">167</td><td align="right">123</td></tr>
  </tbody>
</table>

### Sufficiency & Necessity of MI

For each sample, sufficiency measures whether the top-ranked `MI` (multimodal interaction) features alone preserve the model's confidence in its original answer, whereas necessity measures whether removing them reduces that confidence. Both metrics are normalized against chance level. Results are reported separately for samples whose original prediction was correct or incorrect.

<h4 align="center">Complete Condition</h4>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/qwen_complete_mi_by_correctness.png" style="width: 100%;"/>
    <br/>
    <em>Qwen2.5-Omni</em>
  </div>
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/af3_complete_mi_by_correctness.png" style="width: 100%;"/>
    <br/>
    <em>AudioFlamingo3</em>
  </div>
</div>

<h4 align="center">Text_only condition</h4>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/qwen_audio_only_mi_by_correctness.png" style="width: 100%;"/>
    <br/>
    <em>Qwen2.5-Omni</em>
  </div>
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/af3_audio_only_mi_by_correctness.png" style="width: 100%;"/>
    <br/>
    <em>AudioFlamingo3</em>
  </div>
</div>

<h4 align="center">Audio_only condition</h4>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/qwen_text_only_mi_by_correctness.png" style="width: 100%;"/>
    <br/>
    <em>Qwen2.5-Omni</em>
  </div>
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/af3_text_only_mi_by_correctness.png" style="width: 100%;"/>
    <br/>
    <em>AudioFlamingo3</em>
  </div>
</div>

###  Modality Contributions

For samples where the model's original prediction was correct, we compare sufficiency and necessity across the three feature sources: `UC_text`, `UC_audio`, and `MI`.

- Complete condition
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/qwen_complete_modality_diagnosis.png" style="width: 100%;"/>
    <br/>
    <em>Qwen2.5-Omni</em>
  </div>
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/af3_complete_modality_diagnosis.png" style="width: 100%;"/>
    <br/>
    <em>AudioFlamingo3</em>
  </div>
</div>

- Audio-only condition
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/qwen_audio_only_modality_diagnosis.png" style="width: 100%;"/>
    <br/>
    <em>Qwen2.5-Omni</em>
  </div>
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/af3_audio_only_modality_diagnosis.png" style="width: 100%;"/>
    <br/>
    <em>AudioFlamingo3</em>
  </div>
</div>

- Text-only condition
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/qwen_text_only_modality_diagnosis.png" style="width: 100%;"/>
    <br/>
    <em>Qwen2.5-Omni</em>
  </div>
  <div style="text-align: center; width: 47%;">
    <img src="assets/img/af3_text_only_modality_diagnosis.png" style="width: 100%;"/>
    <br/>
    <em>AudioFlamingo3</em>
  </div>
</div>
<p style="text-align: center; font-size: 0.9em; color: #555;"><em>Note: the Qwen2.5-Omni y-axis reaches 1.4 (instead of 1.0) here because UC_text's sufficiency exceeds 1.0 in this condition and would otherwise be clipped.</em></p>

### Audio Segmentation Example

To verify that the onset-guided segmentation actually produces meaningful, source-specific audio events rather than arbitrary chunks, this section lets you listen to the full segmentation pipeline on one example sample from HumMusQA. The original waveform is first separated into 4 stems (bass, drums, other, vocals) using Demucs; each stem is then split into temporal segments guided by onset detection, giving 4 stems &times; 8 segments = 32 source-segment audio features.

<p>The waveform below each clip shows where in the (silent-padded) audio the segment actually has content. You can see at a glance that each segment lines up with a real, localized event, and you can click directly on the visible waveform to jump there.</p>

<p align="center">
  <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/originale.wav" style="width: 320px;">
    <button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button>
    <span class="wsplayer-wave"></span>
  </span>
</p>
<p align="center"><em>Original audio (HumMusQA sample).</em></p>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 10px;">
  <div style="text-align: center;">
    <div>Bass</div>
    <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/stem_bass.wav" style="width: 180px;">
      <button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button>
      <span class="wsplayer-wave"></span>
    </span>
  </div>
  <div style="text-align: center;">
    <div>Drums</div>
    <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/stem_drums.wav" style="width: 180px;">
      <button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button>
      <span class="wsplayer-wave"></span>
    </span>
  </div>
  <div style="text-align: center;">
    <div>Other</div>
    <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/stem_other.wav" style="width: 180px;">
      <button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button>
      <span class="wsplayer-wave"></span>
    </span>
  </div>
  <div style="text-align: center;">
    <div>Vocals</div>
    <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/stem_vocals.wav" style="width: 180px;">
      <button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button>
      <span class="wsplayer-wave"></span>
    </span>
  </div>
</div>
<p align="center"><em>The four stems separated with Demucs: bass, drums, other, vocals.</em></p>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 24px; margin-top: 10px;">
  <div style="text-align: center;">
    <div>Bass</div>
    <div style="display: flex; flex-direction: column; gap: 4px;">
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_01_bass_seg0.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_05_bass_seg1.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_09_bass_seg2.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_13_bass_seg3.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_17_bass_seg4.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_21_bass_seg5.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_25_bass_seg6.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_29_bass_seg7.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
    </div>
  </div>
  <div style="text-align: center;">
    <div>Drums</div>
    <div style="display: flex; flex-direction: column; gap: 4px;">
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_00_drums_seg0.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_04_drums_seg1.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_08_drums_seg2.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_12_drums_seg3.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_16_drums_seg4.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_20_drums_seg5.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_24_drums_seg6.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_28_drums_seg7.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
    </div>
  </div>
  <div style="text-align: center;">
    <div>Other</div>
    <div style="display: flex; flex-direction: column; gap: 4px;">
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_02_other_seg0.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_06_other_seg1.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_10_other_seg2.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_14_other_seg3.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_18_other_seg4.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_22_other_seg5.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_26_other_seg6.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_30_other_seg7.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
    </div>
  </div>
  <div style="text-align: center;">
    <div>Vocals</div>
    <div style="display: flex; flex-direction: column; gap: 4px;">
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_03_vocals_seg0.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_07_vocals_seg1.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_11_vocals_seg2.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_15_vocals_seg3.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_19_vocals_seg4.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_23_vocals_seg5.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_27_vocals_seg6.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
      <span class="wsplayer" data-wsplayer data-src="assets/audio/sample_01/segmento_31_vocals_seg7.wav" style="width: 100px;"><button class="wsplayer-btn" type="button" aria-label="Play">&#9654;</button><span class="wsplayer-wave"></span></span>
    </div>
  </div>
</div>
<p align="center"><em>The 32 source-segment audio features obtained after onset-guided segmentation (4 stems &times; 8 temporal segments, in chronological order within each stem). Each clip is the full-length reconstruction with only that segment active, so the waveform position shows exactly where the segment sits in time.</em></p>
