import json
from pathlib import Path
from gpt4all import GPT4All, gpt4all


class GPT4AllSession:
    def __init__(self, model_directory, model_name, system_template, prompt_template):
        self.model_directory = model_directory
        self.model_name = model_name
        self.system_template = system_template
        self.prompt_template = prompt_template

    def setup_session(self, placeholders):
        gpt4all.DEFAULT_MODEL_DIRECTORY = self.model_directory
        self.model = GPT4All(self.model_name, allow_download=False)

        if self.model is None:
            raise ValueError("Model not initialized properly.")
        tokens = []
        with self.model.chat_session(self.system_template, self.prompt_template):
            for placeholders_data in placeholders:
                for token in self.model.generate(json.dumps(placeholders_data), temp=0.0, streaming=True):
                    tokens.append(token)
                self.model.current_chat_session.clear()
        tokens_string = ''.join(tokens)
        self.model.close()
        return tokens_string


if __name__ == '__main__':
    system_template = '''Given a JSON document with an array of products, each identified by a unique 'productId' and containing a 'description', generate an enhanced description for each product.Focus on extracting and summarizing factual attributes such as description, ingredients, color, size, dimensions, brand, and sub-brand names. Avoid using superlatives or expressive language.
Provide the most relevant top keyword for each product. The response should be a JSON array with the same number of products as the input, structured as: [{{'productId': int, 'enhancedDescription': string, 'keyword': string}}, ...]'''
    prompt_template = '''{0}'''

    placeholders = [{'productId': 1657, 'description': "This product is Kraft Shredded Mild Cheddar Cheese - 8oz. Mealtime can be challenging, especially pleasing everyone. Kraft Shredded Mild Cheddar Cheese is a solution to make everyone happy. It's backed by Kraft's 100 years of cheese-making experience. This resealable bag of cheese has a rich, creamy flavor, melts easily, and sprinkles evenly. Enhance casseroles, salads, pizzas, and pasta with this shredded cheddar. Made with milk from cows raised without added rbST hormone. Model: 12955126."},
                    {'productId': 1658, 'description': 'Kraft Natural Finely Shredded Mozzarella Cheese, 8 oz. Mealtime made easy and delicious with Kraft Finely Shredded Mozzarella Cheese. Backed by 100 years of quality, this mozzarella adds a special touch to your Italian recipes. Enjoy it on pizzas, pasta, and more.'},
                    {'productId': 1659, 'description': "Kraft Shredded Sharp Cheddar Cheese, 8 oz. A rich, creamy, and easily meltable shredded cheese backed by Kraft's 100 years of expertise. Enhance your family's favorite dishes with this sharp cheddar. Model: 021000055357. Color: Sex Kitten."},
                    {'productId': 1660, 'description': 'Cheez Whiz Original Cheese Snack, 8 oz. Made with real cheese, this snack is an excellent source of calcium. No need to refrigerate. Model: 0002100005556.'}]

    session = GPT4AllSession(Path.cwd(
    ), 'models/mistral-7b-instruct-v0.1.Q4_0.gguf', system_template, prompt_template)
    restult_str = session.setup_session(placeholders)
    print(restult_str)
