#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule


def calculate(_method, n1, n2):
    if _method == 'add':
        return n1 + n2
    elif _method == 'subtract':
        return n1 - n2
    elif _method == 'multiply':
        return n1 * n2
    elif _method == 'divide':
        if n2 == 0:
            return 'INF'
        return n1 / n2
    else:
        return 'INV'


def run_module():
    module_args = dict(
        method=dict(
            type='str',
            required=False,
            default='add',
            choices=['add', 'subtract', 'multiply', 'divide']
        ),
        number1=dict(
            type='int',
            required=True
        ),
        number2=dict(
            type='int',
            required=False,
            default=10
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    _m = module.params['method']
    _i = module.params['number1']
    _j = module.params['number2']

    res = calculate(_m, _i, _j)

    result = dict(
        changed=False,
        msg=res
    )

    if res == 'INF':
        module.fail_json(msg='Division by zero')
    elif res == 'INV':
        module.fail_json(msg='Invalid operation')
    else:
        pass

    module.exit_json(**result)


if __name__ == '__main__':
    run_module()
