import json
import os
from urllib import request

from grabignore import exceptions, settings


class GitignoreFetch:
    def __init__(self):
        self.data = {}
        self.file = settings.IGNORES_FILE

        # Instantiate self.data from file, else fetch
        self.load()

    def parse_data(self, data_list):
        """ Only store ignore files. """
        parsed = {}

        for entry in data_list:
            if ('.gitignore' in entry['name']) and (entry['type'] == 'file'):
                key = entry['name'].lower().replace('.gitignore', '')
                parsed[key] = entry

        return parsed

    def decode_request(self, req):
        """ Decode request binary data to string. """
        return req.read().decode('UTF-8')

    def fetch(self):
        """ Fetch gitignores and store internally. """
        res = request.urlopen(settings.URL)

        if res.code != 200:
            raise exceptions.RequestError(
                f'Error fetching gitignore data')

        # Decode binary data and convert from json
        json_data = json.loads(self.decode_request(res))
        return self.parse_data(json_data)

    def write(self):
        """  Write data to external json file. """

        with open(self.file, mode='w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def load(self):
        """ Load contents of json file to self.data. """
        if not os.path.isfile(self.file):
            self.data = self.fetch()
            self.write()
            return

        self.data = json.load(open(self.file))

    def update(self):
        """ Update the file with a fresh fetch. """
        new_data = self.fetch()

        if new_data != self.data:
            # Overwrite file with new data
            self.data = new_data
            self.write()

    def download(self, gitignore_name, destination='.',
                 output_file='.gitignore', ignore_output_name=False):
        try:
            gitignore_name = gitignore_name.lower().strip()
            download_url = self.data[gitignore_name]['download_url']

            # If ignore flag is True, use the original gitignore file name
            if ignore_output_name:
                output_file = self.data[gitignore_name]['name']

            output_file = os.path.join(
                os.path.abspath(os.path.expanduser(destination)), output_file)

            res = request.urlopen(download_url)

            if res.code != 200:
                raise exceptions.RequestError(
                    f'Failed to fetch file {gitignore_name}')

            data = self.decode_request(res)
            with open(output_file, 'w') as outfile:
                outfile.write(data)

        except KeyError:
            raise exceptions.InvalidGitignoreError((
                f'A gitignore file for {gitignore_name} '
                'is not currently supported.'))
        except Exception as e:
            raise e
