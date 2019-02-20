# -*- coding: utf-8 -*-
## (C) 2019 Muthiah Annamalai,
import unittest

from snowballstemmer import algorithms, stemmer

class Simple(unittest.TestCase):
    def test_symbols(self):
        self.assertTrue( globals().has_key('algorithms') )
        self.assertTrue( globals().has_key('stemmer') )
        
    def test_algos(self):
        expected = ['danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish', 'tamil', 'turkish']
        self.assertEqual( expected, algorithms() )


class TamilTest(unittest.TestCase):
    def __init__(self,*args):
        unittest.TestCase.__init__(self,*args)
        self.ta_stemmer = stemmer('tamil')
        self.assertTrue( self.ta_stemmer != None )
        
    def test_suffix(self):
        wordlist = [u'மலைகள்',u'பாடுதல்',u'ஓடினான்']
        expected = [u'மலை',u'பாடு', u'ஓடி']
        stems = [self.ta_stemmer.stemWord(word) for word in wordlist]
        self.assertSequenceEqual( stems, expected )

if __name__ == "__main__":
    unittest.main()
