import itertools
import re

import numpy as np

from app.api.db import outlet_data


class RegexMatcher:
    """Class to compute regex matches on meal delivery data.

    Searches whether the specified column name of the item contains a whole word.
    Similar to 'contain', but it looks for the whole word.

    Args:
        search_word: word to search for
    """

    def __init__(self, search_word: str):

        # regex expression to search if word is contained
        self.regexp = r'(?:^|\\W){}(?:$|\\W)'.format(search_word)

        # by default outlet_data is used
        self.dataset = outlet_data

        # define search word
        self.search_word = search_word

    def _compute_matches(self, column_name: str):

        # applying regex search and returning match indices
        result = [bool(re.search(self.regexp, str(word))) for word in self.dataset[column_name]]

        indices = np.where(result)[0]

        # get list of matched instances
        match_list = self.dataset.iloc[indices, :][["id_source"]].drop_duplicates().values.tolist()

        # flatten the list of lists
        merged = list(itertools.chain(*match_list))

        return merged

    def get_matches(self, column_name: str):
        """Get all matches and on column name

        Args:
            column_name: Name of the column to run regex query on

        Returns:
            Dictionary holding regex query, search word, and list of outlets
            which contain search word in the specified column name.

        """

        # get all unique outlets which contain word in specified column name
        matched_outlets = self._compute_matches(column_name)

        # number of unique outlets
        num_unique_outlets = len(self.dataset["id_source"].drop_duplicates())

        # Build response dictionary
        match_dict = dict(
            regex_query=self.regexp,
            search_word=self.search_word,
            num_outlets=len(matched_outlets),
            per_outlets=round((len(matched_outlets) / num_unique_outlets * 100), 2),
            brand_id=matched_outlets
        )

        return match_dict
