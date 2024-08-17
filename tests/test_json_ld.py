import unittest
from pathlib import Path

from recipy.json_ld import recipe_from_json


class TestJsonLd(unittest.TestCase):
    def test_recipe_from_json(self):
        failures = []
        success_count = 0

        for json_file in Path(__file__).parent.glob('test_data/*.json'):
            with open(json_file, 'r') as f:
                recipe = recipe_from_json(f.read())
                if recipe is None:
                    failures.append(json_file)
                else:
                    success_count += 1

        failed_count = len(failures)
        print(f"Success: {success_count}")
        print(f"Failed: {failed_count}")

        if failures:
            print("Failures:")
            for failure in failures:
                if isinstance(failure, tuple):
                    print(f" - {failure[0]}: Exception: {failure[1]}")
                else:
                    print(f" - {failure}")

        self.assertEqual(failed_count, 0)


if __name__ == '__main__':
    unittest.main()
