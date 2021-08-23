# timeseries-anomaly-detection

<!--
*** Written by Martin Karlsson
*** www.martinkarlsson.io
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- ABOUT THE PROJECT -->
## About The Project

![Plot of data and anomaly rating](plot-output-small)

Purpose for this tutorial is to show how to easily utilize a Robust Random Cut Forest neural network to find anomalies in time series data.
It will utilize multiprocessing to efficiently run multiple RCCF processes in parallell. This will decrease the execution time.


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

Martin Karlsson - [@HelloKarlsson](https://twitter.com/HelloKarlsson) - hello@martinkarlsson.io
[www.martinkarlsson.io](https://www.martinkarlsson.io)

Project Link: https://github.com/martinkarlssonio/timeseries-anomaly-detection](https://github.com/martinkarlssonio/timeseries-anomaly-detection)



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/martin-karlsson
[plot-output-small]: images/plot_output_small.png