# Cyber Security

> Cyber Security related self-learnings. _CMPT 318: Cyber Security_ can be found [Here](https://github.com/alik604/Classes/tree/master/CMPT318)

## Projects Here

### Network Intrusion Detection

  * KDD cup ‘99
    * [100% Accuracy](https://github.com/alik604/cyber-security/blob/master/anomalyDetection/KDD%20cup%20'99/kddcup_99_100accAchieved.ipynb)
    * [Blog post](https://medium.com/@alik604/predicting-the-nsl-kdd-data-set-with-98-accuracy-240a7a245c9d)
  * NSL-KDD (corrected dataset based off KDD cup ‘99’)
    * [98% Accuracy](https://github.com/alik604/cyber-security/blob/master/Intrusion-Detection/NSL_KDD/NSL_KDD.ipynb)
    * [Effects of Dimensionality Reduction](https://github.com/alik604/dimensionality-reduction-overview) 
    * [Blog post](https://medium.com/@alik604/dimensionality-reduction-effects-on-model-accuracy-c021f4f33a61)
  * UNSW_NB15
    * [94.8% Accuracy](https://github.com/alik604/cyber-security/blob/master/Intrusion-Detection/UNSW_NB15.ipynb)
      * 91% Accuracy with a **feedforward neural network**, 94.8% with **Ensemble** (of non neural network techniques, 'voting')
      * Autoencoder of Anomaly Detection
      * Upsupervised with [PYOD](https://github.com/yzhao062/pyod), which is a "A Python Toolbox for Scalable Outlier Detection (Anomaly Detection)"
### Financial Anomaly Detection
   * SPX 500 pointing out _oddities_ from the past in an unsupervised manner
     * Some argue the stock market is a random signal, which tends to have a positive trend in the *long run*. So, I tried Anomaly Detection on it. Perhaps it's an *extream* **bull run** and **bear run** detector

### Utilities
  * [Rainbow Table of several Hashing Algorithms](https://github.com/alik604/cyber-security/tree/master/Utilities/Rainbow-table-of-serval-hashing-algorithms)* A simple hash lookup table
  * [Bandwidth Hog](https://github.com/alik604/cyber-security/tree/master/Utilities/bandwidth-hog)
    * Download a file many times, but do not save the data. Useful for stressing out a network... possibly your own
  * File (de)Encryption
    * boilerplate code for my latter use  
  * unExpectedProcessChecker
    * outputs the mutually exclusive set of processes, given set A, which is hardcoded, and set B, which is from the windows environment being run on
  * Simple keylogger
  * Dos script

## Related projects

1. [CMPT 318: Cyber Security](https://github.com/alik604/Classes/tree/master/CMPT318)
   * [Presentation on Anomaly Detection](https://github.com/alik604/Classes/blob/master/CMPT318/CMPT_318_Presentation.pdf)
2. [myPybackdoor](https://github.com/alik604/myPybackdoor)
   * Navigate Directories
   * Download, Create, and Delete Files
   * Execute custom CMD commands
   * Get wifi Password list
3. [chromePasswordThief](https://github.com/alik604/chrome-password-thief)
   * Grab passwords saved in chrome and email them out
   * [Blog post](https://alik604.github.io/chrome-password-thief/index.html)
4. [bandwidth-hog](https://github.com/alik604/bandwidth-hog)
   * Download a file many times, but do not save the data. Useful for stressing out a network... possibly your own
5. [Rainbow table of serval hashing algorithm](https://github.com/alik604/Rainbow-table-of-serval-hashing-algorithm)
   
   * A simple hash lookup table, easily expandable to fit your needs
