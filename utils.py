import configparser

def load_characters(config_path):
    parser = configparser.ConfigParser()
    parser.read(config_path)
    chars = {}
    for sec in parser.sections():
        basic = parser.getint(sec, 'basic_attack')
        skills = {i: parser.getint(sec, f'skill{i}_attack') for i in range(1, 6)}
        chars[sec] = {'basic': basic, 'skills': skills}
    return chars