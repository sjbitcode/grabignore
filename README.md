# grabignore
Python CLI to grab a gitignore any gitgnore file.

## Usage
`python3 -m grabignore [languages] --dest=/some/destination --reload=True`

- languages: gitignore files you want to fetch.
- dest (optional): path where you want files to be downloaded to. Defaulted to current directory.
- reload (optional): flag to initiate a fresh batch of gitignore files to download from. Defaulted to false.

*Note:* The file name is defaulted to `.gitignore` if only one language is passed to the cli. If multiple languages are passed, then files will be names as the language name (`Python.gitgnore`).

## Example usages
`python3 -m grabignore python`

`python3 -m grabignore python node ruby`

`python3 -m grabignore node --dest=/app/myproject`

`python3 -m grabignore node ruby reload=True`

