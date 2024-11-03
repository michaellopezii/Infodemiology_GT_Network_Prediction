# Introduction

This is the official repository for the undergraduate thesis of Lopes and Hung (2024). The following folders are here for you to explore:

1. `gt_scraper`: These are the `python` programs that helped us on scraping off Google Trends data from the internet. It came from an open-sourced program by Chu et al.
2. `gt_raw_daily30daywindow_volumes`: Where you may find the raw GT values in 30-day windows for each keyword.
3. `gt_preprocessed_data`: This is where the conversion of each GT data into RSV and MSV.
4. `gt_corr_adj_matrix`: Where the calculated 15 by 15 distance correlation matrices can be found each for RSV and MSV processed GT data. Used the `dcorr` python import package to perform this.
5. `gt_netdense_cluscoeff`: Where the network density and clustering coefficient of the entire 15 keyword bank can be seen. It has four thresholds: 0.4, 0.5, 0.6, and 0.8.
6. `gt_corr_adj_matrix`: Where the adjacency matrices for the entire network at different thresholds can be seen. 
7. `gt_pca_analysis`: Where the PCA computation was conducted
8. `gt_pca_corr_adj_matrix`: Calculcated here the corresponding adjacency matrix for each PCA group. We did not considered calculating for the adjacency matrix of the PCA groups that have equal to or fewer than 3.
9. `gt_dtw_calculation`: Where the dynamic time warping was implemented.

# PCA Groups
## With 0.6 Thresholds
* MSVSymptoms-0.6: cough, fever, sipon
* MSVNewNormalProtocols1-0.6: ecq, quarantine
* MSVNewNormalProtocol2-0.6: work from home NOPE
* MSVSymptoms&NewNormalProtocols-0.6: flu, headache, lagnat, rashes, ubo, face shield, frontliners, masks, social distancing
* RSVSymptoms&NewNormalProtocols1-0.6: flu, cough, fever, quarantine, work from home
* RSVNewNormalProtocol1-0.6: ecq
* RSVSymptoms&NewNormalProtocols2-0.6: face shield, headache, lagnat, rashes, sipon, ubo, frontliners, masks, social distancing

## With 0.5 Thresholds
* MSVSymptoms-0.5: flu, cough, fever, sipon, ubo
* MSVNewNormalProtocols1-0.5: quarantine, frontliners, ecq
* MSVNewNormalProtocol2-0.5: work from home
* MSVFaceWearing&Others-0.5: masks, face shield, headache, lagnat, rashes, social distancing
* RSVSymptoms&NewNormalProtocols-0.5: social distancing, work from home, quarantine, headache, fever, cough, flu
* RSVNewNormalProtocol-0.5: ecq
* RSVFaceWearing&Others-0.5: face shield, masks, frontliners, ubo, sipon, rashes, lagnat