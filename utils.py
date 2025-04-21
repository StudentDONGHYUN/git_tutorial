import configparser

def load_characters(config_path):
    """
    Load character stats from a configuration file.
    구성 파일에서 캐릭터 능력치를 로드합니다.

    Args:
        config_path (str): Path to the INI-style configuration file.
            INI 형식 구성 파일의 경로입니다.

    Returns:
        dict[str, dict]:
            A mapping where each key is a section name and each value is a dict with:
                basic (int): The basic attack value.
                skills (dict[int, int]): Mapping of skill indices (1–5) to their attack values.
            키는 섹션 이름, 값은 다음 키를 갖는 딕셔너리:
                basic (int): 기본 공격력.
                skills (dict[int, int]): 스킬 인덱스(1~5)의 공격력 매핑.

    Raises:
        configparser.Error: If the configuration file cannot be read or parsed.
            구성 파일을 읽거나 구문 분석할 수 없는 경우 발생합니다.
    """
    parser = configparser.ConfigParser()
    parser.read(config_path)
    chars = {}
    for sec in parser.sections():
        basic = parser.getint(sec, 'basic_attack')
        skills = {i: parser.getint(sec, f'skill{i}_attack') for i in range(1, 6)}
        chars[sec] = {'basic': basic, 'skills': skills}
    return chars