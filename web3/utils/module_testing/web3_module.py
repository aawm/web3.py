import pytest


class Web3ModuleTest(object):
    def test_web3_clientVersion(self, web3):
        client_version = web3.version.node
        self._check_web3_clientVersion(client_version)

    def _check_web3_clientVersion(self, client_version):
        raise NotImplementedError("Must be implemented by subclasses")

    # Contract that calculated test values can be found at
    # https://kovan.etherscan.io/address/0xb9be06f5b99372cf9afbccadbbb9954ccaf7f4bb#code
    @pytest.mark.parametrize(
        'types,values,expected',
        (
            (
                ['bool'],
                [True],
                "0x5fe7f977e71dba2ea1a68e21057beebb9be2ac30c6410aa38d4f3fbe41dcffd2",
            ),
            (
                ['uint8', 'uint8', 'uint8'],
                [97, 98, 99],
                "0x4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45",
            ),
            (
                ['uint248'],
                [30],
                "0x30f95d210785601eb33ae4d53d405b26f920e765dff87cca8e9a4aec99f82671",
            ),
            (
                ['bool', 'uint16'],
                [True, 299],
                "0xed18599ccd80ee9fae9a28b0e34a5573c3233d7468f808fd659bc171cf0b43bd",
            ),
            (
                ['int256'],
                [-10],
                "0xd6fb717f7e270a360f5093ce6a7a3752183e89c9a9afe5c0cb54b458a304d3d5",
            ),
            (
                ['int256'],
                [10],
                "0xc65a7bb8d6351c1cf70c95a316cc6a92839c986682d98bc35f958f4883f9d2a8",
            ),
            (
                ['int8', 'uint8'],
                [-10, 18],
                "0x5c6ab1e634c08d9c0f4df4d789e8727943ef010dd7ca8e3c89de197a26d148be",
            ),
            (
                ['address'],
                ["0x49eddd3769c0712032808d86597b84ac5c2f5614"],
                "0x2ff37b5607484cd4eecf6d13292e22bd6e5401eaffcc07e279583bc742c68882",
            ),
            (
                ['bytes2'],
                ['0x5402'],
                "0x4ed9171bda52fca71ab28e7f452bd6eacc3e5a568a47e0fa53b503159a9b8910",
            ),
            (
                ['bytes3'],
                ['0x5402'],
                "0x4ed9171bda52fca71ab28e7f452bd6eacc3e5a568a47e0fa53b503159a9b8910",
            ),
            (
                ['bytes'],
                [
                    '0x636865636b6c6f6e6762797465737472696e676167'
                    '61696e7374736f6c6964697479736861336861736866756e6374696f6e'
                ],
                "0xd78a84d65721b67e4011b10c99dafdedcdcd7cb30153064f773e210b4762e22f",
            ),

            (
                ['string'],
                ['testing a string!'],
                "0xe8c275c0b4070a5ec6cfcb83f0ba394b30ddd283de785d43f2eabfb04bd96747",
            ),
            (
                ['string', 'bool', 'uint16', 'bytes2', 'address'],
                [
                    'testing a string!',
                    False,
                    299,
                    '0x5402',
                    "0x49eddd3769c0712032808d86597b84ac5c2f5614",
                ],
                "0x8cc6eabb25b842715e8ca39e2524ed946759aa37bfb7d4b81829cf5a7e266103",
            ),
            (
                ['bool[2][]'],
                [[[True, False], [False, True]]],
                "0x1eef261f2eb51a8c736d52be3f91ff79e78a9ec5df2b7f50d0c6f98ed1e2bc06",
            ),
            (
                ['bool[]'],
                [[True, False, True]],
                "0x5c6090c0461491a2941743bda5c3658bf1ea53bbd3edcde54e16205e18b45792",
            ),
            (
                ['uint24[]'],
                [[1, 0, 1]],
                "0x5c6090c0461491a2941743bda5c3658bf1ea53bbd3edcde54e16205e18b45792",
            ),
            (
                ['uint8[2]'],
                [[8, 9]],
                "0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538a",
            ),
            (
                ['uint256[2]'],
                [[8, 9]],
                "0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538a",
            ),
            (
                ['uint8[]'],
                [[8]],
                "0xf3f7a9fe364faab93b216da50a3214154f22a0a2b415b23a84c8169e8b636ee3",
            ),
            (
                ['address[]'],
                [[
                    "0x49EdDD3769c0712032808D86597B84ac5c2F5614",
                    "0xA6b759bBbf4B59D24acf7E06e79f3a5D104fdCE5",
                ]],
                "0xb98565c0c26a962fd54d93b0ed6fb9296e03e9da29d2281ed3e3473109ef7dde",
            ),
        ),
    )
    def test_soliditySha3(self, web3, types, values, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                web3.soliditySha3(types, values)
            return

        actual = web3.soliditySha3(types, values)
        assert actual == expected

    @pytest.mark.parametrize(
        'types,values',
        (
            (['address'], ['0xA6b759bBbf4B59D24acf7E06e79f3a5D104fdCE5', True]),
            (['address', 'bool'], ['0xA6b759bBbf4B59D24acf7E06e79f3a5D104fdCE5']),
            ([], ['0xA6b759bBbf4B59D24acf7E06e79f3a5D104fdCE5']),
        )
    )
    def test_soliditySha3_same_number_of_types_and_values(self, web3, types, values):
        with pytest.raises(ValueError):
            web3.soliditySha3(types, values)
