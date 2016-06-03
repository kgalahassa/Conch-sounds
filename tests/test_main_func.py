import pytest

from acousticsim.main import (acoustic_similarity_mapping,
                                        acoustic_similarity_directories,
                                        analyze_directory, analyze_long_file)


slow = pytest.mark.skipif(
    not pytest.config.getoption("--runslow"),
    reason="need --runslow option to run"
)

@slow
def test_analyze_directory(soundfiles_dir, call_back):
    kwargs = {'rep': 'mfcc','win_len': 0.025,
                'time_step': 0.01, 'num_coeffs': 13,
                'freq_lims': (0,8000),'return_rep':True,
                'use_multi':True}
    scores,reps = analyze_directory(soundfiles_dir, call_back = call_back,**kwargs)


def test_analyze_long_file_reaper(acoustic_corpus_path, reaper_func):
    segments = [(1, 2, 0)]
    output = analyze_long_file(acoustic_corpus_path, segments, reaper_func)

def test_analyze_long_file_formants(acoustic_corpus_path, formants_func):
    segments = [(1, 2, 0)]
    output = analyze_long_file(acoustic_corpus_path, segments, formants_func)
