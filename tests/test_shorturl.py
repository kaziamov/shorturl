from shorturl.main import DEFAULT_LENGTH, DEFAULT_SYMBOLS, generate_link, generate_path

def test_generate_path_lenght():
    assert len(generate_path()) == DEFAULT_LENGTH

def test_generate_custom_link():
    assert generate_link(custom='hello') == 'hello'