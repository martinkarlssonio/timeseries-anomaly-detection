# Anomaly Detection in Time-Series Data
### Using Robust Random Cut Forest and Multiprocessing

<!--
*** Written by Martin Karlsson
*** www.martinkarlsson.io
-->

[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- ABOUT THE PROJECT -->
## About The Project

Purpose for this tutorial is to show how to easily utilize a Robust Random Cut Forest neural network to find anomalies in time series data. \
It utilizes multiprocessing to efficiently run multiple RCCF processes in parallell. This will decrease the execution time.


![Plot of data and anomaly rating][plot-output-small]


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python pip packages
  ```sh
  python3 -m pip install -r requirements.txt
  ```


<!-- USAGE EXAMPLES -->
## Usage

* Run the code
  ```sh
  python3 main.py
  ```

<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/featureName`)
3. Commit your Changes (`git commit -m 'Add some featureName'`)
4. Push to the Branch (`git push origin feature/featureName`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

### Martin Karlsson

LinkedIn : [martin-karlsson][linkedin-url] \
Twitter : [@HelloKarlsson](https://twitter.com/HelloKarlsson) \
Email : hello@martinkarlsson.io \
Webpage : [www.martinkarlsson.io](https://www.martinkarlsson.io)


Project Link: [github.com/martinkarlssonio/timeseries-anomaly-detection](https://github.com/martinkarlssonio/timeseries-anomaly-detection)



<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/martin-karlsson
[plot-output-small]: images/plot_output_small.png