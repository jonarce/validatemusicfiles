# validatemusicfiles
Script to validate incomming music files to be added to a library. It will check certain aspect of it, but can be configured in its config.yaml file.
Filename:
  - Check if filename has invalid characters and will rename it based on your own transliteration rules (as defined in the config.yaml file)
  - for example I delete characters as: ~`!@$%^&*, but change "#" to be "no".
  -                   change "&" to be "and", and change all accent vowels to be the same vowel without accent.
                      check if checksum is in the file, if not it will unconvert (back to wav) and reconvert adding it
                      replace other language characters for their English equivalent
  - embedded art vs cover file in its directory, will extract it if required
  - art image size, you can set the acceptable minimum size to check

FLAC format:
  - checksum - vhevk if the file contains its checksum, if not it will decompress / recompress with it
  - oversampling - check if the file is suspected to be an oversampling (relies in external code)

Virtual Enviroment:
To create a virtual environment yourself you can use Python's venv:

python -m venv my-venv
my-venv/bin/pip install some-python-library

for this project it is: validatemusicfiles/bin/python3 chevkmusivfiles.py

