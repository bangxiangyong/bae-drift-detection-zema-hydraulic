# Bayesian autoencoders for drift detection in industrial environments

Development of Bayesian Autoencoders to  quantify  epistemic  and  aleatoric  uncertainties, within the context of real and virtual drifts in industrial sensors.

## Dataset

We use a hydraulic condition monitoring dataset recorded at ZEMA Testbed: https://archive.ics.uci.edu/ml/datasets/Condition+monitoring+of+hydraulic+systems

## Acknowledgement

The research presented was supported by European Metrology Programme for Innovation and Research (EMPIR) under the project Metrology for the Factory of the Future (MET4FOF), project number 17IND12 as well as the PITCH-IN (Promoting the Internet of Things via Collaborations between HEIs and Industry) project funded by Research England.  We express our gratitude to Tim Pearce for his inputs. 

## Uncertainty of reconstructed signals

Uncertainties of reconstructed signals in presence of real drifts (degrading cooler condition), and virtual drifts (injected noise and drift in one of pressure sensors, PS1)

![Uncertainties of Reconstructed signals](https://github.com/bangxiangyong/bae-drift-detection-zema-hydraulic/blob/master/figures_bae_zema/RECON-SIG.png)

## Sensitivity analysis

Sensitivity of reconstruction loss, epistemic uncertainty and aleatoric uncertainty towards drifts.

![Real drift](https://github.com/bangxiangyong/bae-drift-detection-zema-hydraulic/blob/master/figures_bae_zema/REAL-DRIFT.png)

![Virtual drift-noise](https://github.com/bangxiangyong/bae-drift-detection-zema-hydraulic/blob/master/figures_bae_zema/INJECTED-NOISE.png)

![virtual drift-sensordrifts](https://github.com/bangxiangyong/bae-drift-detection-zema-hydraulic/blob/master/figures_bae_zema/INJECTED-DRIFT.png)


