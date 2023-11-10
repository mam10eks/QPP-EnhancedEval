from qpptk import main, parse_args
import tempfile
import pandas as pd

def test_end_to_end():
    with tempfile.TemporaryDirectory() as out_dir, tempfile.TemporaryDirectory() as stats_dir:
        args = parse_args(['-ti', 'tests/resources/small-example-01/index/', '--jsonl_queries', 'tests/resources/small-example-01/queries.jsonl', '--predict', '--retrieve', '--output', out_dir, '--cleanOutput','--stats_index_path',  stats_dir])
        main(args)

        actual = pd.read_json(out_dir + '/queries.jsonl', lines=True)

        assert len(actual) == 3

        assert actual.iloc[0].to_dict()['avg-idf'] == 1.3296613489
        assert actual.iloc[0].to_dict()['avg-scq'] == 2.2134369757
        assert actual.iloc[0].to_dict()['clarity+1000+3'] == 2.6980214786000003
        assert actual.iloc[0].to_dict()['max-idf'] == 1.7917594692

        assert actual.iloc[1].to_dict()['avg-idf'] == 1.0986122887
        assert actual.iloc[1].to_dict()['avg-scq'] == 2.909294382
        assert actual.iloc[1].to_dict()['max-idf'] ==  1.0986122887

        assert actual.iloc[2].to_dict()['avg-idf'] == 1.0986122887
        assert actual.iloc[2].to_dict()['avg-scq'] == 2.6282473855
        assert actual.iloc[2].to_dict()['max-idf'] ==  1.0986122887