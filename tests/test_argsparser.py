from argparse import ArgumentParser
from mi_parser import setup_parser


class TestArgsParser:
    def setup_method(self):
        parser = ArgumentParser()
        self.mi_parser = setup_parser(parser)

    def test_parses_visual_option(self):
        args = ['-v']

        parser = self.mi_parser.parse_args(args)

        assert parser.visualisation == True

    def test_visual_have_help(self):
        helper_msg = self.mi_parser.format_help()

        assert "visualise the graph" in helper_msg






















