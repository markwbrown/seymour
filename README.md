
<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/markwbrown/seymour">
    <img src="seed_me.jpg" alt="AI Generated Art of Audrey II from Little Shop of Horrors with a rotary phone" width="180">
  </a>

<h3 align="center">Seymour</h3>

  <p align="left">
    SEED ME! Seymour is a tiny python script to seed a postgres database running in docker on one's local based upon values defined in the .env file in a project's root. It grabs the port docker exposes for a container running postgres from docker-config.yml and updates values in a table. It isn't rocket surgery, but it was a handy tool to quickly get values plugged into a database for testing a two-factor authentication flow refactor. It should serve as a useful starting point to get variables from a .env file into a database. The project name came from Audrey II's "FEED ME' line to Seymour in Little Shop of Horrors because we're seeding a database and the image came from DALL-E with the prompt "Audrey 2 from Little Shop of Horrors with a rotary phone.", because you know... two factor. 
  </p>
</div>



<!-- GETTING STARTED -->
## Getting Started

1. drop the main.py and requirements.txt into your project root.
2. copy .sample_env to .env and update with your desired 2fa variables
3.  `pip install`
4. `python main.py`

### Prerequisites

python
a database running in docker locally
some values you wish to seed the database with

<!-- USAGE EXAMPLES -->
## Usage
`python main.py`

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
6. Come work with me at [Summit Technology Consulting Group](https://thesummitgrp.com)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.