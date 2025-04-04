## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

#Answer 1

Data may not have been recorded (missing/NO DATA), due to a variety of reasons such as 
1. Device malfunction, where the battery may have died, the user may have accidentally turned it off, or removed it. 
2. File corruption 
3. Syncing issues, where there could've been connectivity issues such as WIFI/Bluetooth disruptions 

Filtering out missing or "NO DATA" values might introduce bias into the analysis. These gaps could point to underlying issues with the device itself, which would be important to highlight in the final report. Also, the pattern of missing data could support hypotheses, for example, whether gaps occur more often during rest or physical activity. By not including this information, there is a risk of overlooking meaningful trends and ending up with an incomplete analysis. It is best to treat it as a category on it's own to give a complete picture of the data sampled.   


## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

#Answer 2 

Sleep occurs in phase 0. Phase 0 has the lowest maximum heart rate of 93 BPM, which is the lowest of all heart rates in all 4 phases. It also has the lowest standard deviation of 8.53, indicating minimal variability of activity such as sleeping. This analysis is also supported by the graph showing less dramatic spikes compared to other phases.  

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

#Answer 3 

Exercise likely occurs during the first and second phases. The maximum heart rates in both phases are above 100 BPM, with phase 1 being 110 BPM and phase 2 as 117 BPM. Also, compared to the other phases, they have the highest average heart rates, with phase 1 and phase 2 recording 87.3 BPM and 85.18 BPM, respectively. Thus highlighting an increase in strenuous activity leading to a rise in heart rate. The visuals also support this claim; for example, phase 2 shows more frequent fluctuations and higher values. 


## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

Answer 4 
Phase 3 exhibits periods of awake activity, with the lowest average heart rate of 60.65 BPM, indicating rest mode compared to all other phases. It also has a relatively higher standard deviation of 11.0, meaning there is more variability, which is supported by the graph, suggesting different activities happening while the person is awake, walking, eating, running, watching TV, etc. 
