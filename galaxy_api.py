import os

from bioblend.galaxy import GalaxyInstance


def get_environment_variables():
    base_url = os.getenv('GALAXY_BASE_URL') or 'https://galaxy.hyphy.org'
    api_key = os.getenv('GALAXY_API_KEY')
    return (base_url, api_key)
    

def create_rga_history(accession, references):
    base_url, api_key = get_environment_variables()
    gi = GalaxyInstance(base_url, key=api_key)
    result = gi.histories.create_history('bioblend test')
    print(result)


if __name__ == '__main__':
    create_rga_history('SRR7167618', './input/sudan-ebola-ncbi.fasta')
