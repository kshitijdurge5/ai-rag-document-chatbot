from app import answer_question

def test_retrieves_matching_line():
    r = answer_question('refund policy', 'Refunds take five days.\nShipping is tracked.')
    assert 'Refunds' in r['answer']

def test_no_match_is_explicit():
    assert 'No matching' in answer_question('quantum', 'Refunds take five days.')['answer']
