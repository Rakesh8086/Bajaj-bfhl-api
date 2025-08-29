from flask import Flask, request, jsonify
from collections import OrderedDict

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get('data', [])

        odd_numbers = []
        even_numbers = []
        alphabets = []
        
        numeric_sum = 0
        
        for item in data:
            if isinstance(item, str):
                if item.isdigit():
                    num = int(item)
                    if num % 2 == 0:
                        even_numbers.append(item)
                    else:
                        odd_numbers.append(item)
                    numeric_sum += num
                elif item.isalpha():
                    alphabets.append(item)

        special_characters = [item for item in data if isinstance(item, str) and not item.isalnum()]
        
        uppercase_alphabets = [char.upper() for char in alphabets]

        combined_alphabets = "".join(alphabets)
        
        alphabets_reversed = combined_alphabets[::-1]
        
        concat_string = ""
        for i, char in enumerate(alphabets_reversed):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()

        response = OrderedDict()
        response["is_success"] = "true"
        response["user_id"] = "john_doe_17091999"
        response["email"] = "john@xyz.com"
        response["roll_number"] = "ABCD123"
        response["odd_numbers"] = odd_numbers
        response["even_numbers"] = even_numbers
        response["alphabets"] = uppercase_alphabets
        response["special_characters"] = special_characters
        response["sum"] = str(numeric_sum)
        response["concat_string"] = concat_string
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)