from settings import OPERATOR_LIST


def append_token(stack, state, output_list):

    token  = ''.join(stack)

    if state.__name__ in ['num_pre_dot_state', 'num_post_dot_state']:
        token_value = float(token)
        token_type = 'NUMBER'

    elif state.__name__ in ['sym_state', 'div_state', 'mul_state',
                            'comma_state', 'plus_state', 'minus_state',
                            'plus_post_operator_state', 'minus_post_operator_state',
                            'artificial_mul_state']:
        token_value = None
        token_type = 'OPERATOR'

    elif state.__name__ == 'word_state':
        if token in OPERATOR_LIST:
            token_value = None
            token_type = 'OPERATOR'
        else:
            raise Exception('Undefined operator: {}'.format(token))

    else:
        raise Exception('Unknown state: {}'. format(state))

    output_list.append(
        {'name': token,
         'value': token_value,
         'type': token_type
        }
    )


if __name__ == '__main__':
    from tokenizer_FSM import num_post_dot_state

    output_list = []
    stack = ['1', '.', '2']
    token_type = "NUMBER"

    append_token(stack, num_post_dot_state, output_list)
    print(output_list)