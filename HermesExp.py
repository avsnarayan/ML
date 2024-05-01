
from hermes import Hermes

# Load the model
hermes = Hermes("Hermes 2 Pro - Mistral 7B")

# Sample data
data = [
    {"productId": 1657,
     "description": "This product is Kraft Shredded Mild Cheddar Cheese - 8oz. Mealtime can be challenging, especially pleasing everyone. Kraft Shredded Mild Cheddar Cheese is a solution to make everyone happy. It's backed by Kraft's 100 years of cheese-making experience. This resealable bag of cheese has a rich, creamy flavor, melts easily, and sprinkles evenly. Enhance casseroles, salads, pizzas, and pasta with this shredded cheddar. Made with milk from cows raised without added rbST hormone. Model: 12955126."},
    {"productId": 1658,
     "description": 'Kraft Natural Finely Shredded Mozzarella Cheese, 8 oz. Mealtime made easy and delicious with Kraft Finely Shredded Mozzarella Cheese. Backed by 100 years of quality, this mozzarella adds a special touch to your Italian recipes. Enjoy it on pizzas, pasta, and more.'},
    {"productId": 1659,
     "description": "Kraft Shredded Sharp Cheddar Cheese, 8 oz. A rich, creamy, and easily meltable shredded cheese backed by Kraft's 100 years of expertise. Enhance your family's favorite dishes with this sharp cheddar. Model: 021000055357. Color: Sex Kitten."},
    {"productId": 1660,
     "description": 'Cheez Whiz Original Cheese Snack, 8 oz. Made with real cheese, this snack is an excellent source of calcium. No need to refrigerate. Model: 0002100005556.'}
]

# Define the system and prompt templates
system_template = '''Given a JSON document with an array of products, each identified by a unique 'productId' and containing a 'description', generate an enhanced description for each product. Focus on extracting and summarizing factual attributes such as description, ingredients, color, size, dimensions, brand, and sub-brand names. Avoid using superlatives or expressive language. Provide the most relevant top keyword for each product. The response should be a JSON array with the same number of products as the input, structured as: [{"productId": int, "enhancedDescription": string, "keyword": string}, ...]'''

prompt_template = '''{}'''

# Combine the system and prompt templates
prompt = prompt_template.format(system_template)

# Generate the enhanced descriptions and keywords using the model
enhanced_data = hermes(prompt, data)

# Print the results
for item in enhanced_data:
    print(f"Product ID: {item['productId']}")
    print(f"Enhanced Description: {item['enhancedDescription']}")
    print(f"Keyword: {item['keyword']}")
    print()