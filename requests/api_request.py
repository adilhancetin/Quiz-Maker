from flask import Flask,request
import openai_request
app = Flask(__name__)

@app.route('/test')
def test():
    return "Server is running!"


@app.route('/quiz', methods=['GET'])
def display_quiz():
    topic = request.args.get('topic')
    questions = openai_request.make_openai_request(topic)

    quiz_list = generate_quiz(questions)
    return quiz_list


def generate_quiz(questions):
    parts = questions.strip().split("\n\n")
    answer_part = parts[-1].split(":")[1].strip()
    parts = parts[:-1]
    quiz_list = []
    
    for i, block in enumerate(parts):
        lines = block.strip().split("\n")
        
        question_text = lines[0][3:].strip()
        options = {
            'a': lines[1].split(') ')[1].strip(),  
            'b': lines[2].split(') ')[1].strip(),  
            'c': lines[3].split(') ')[1].strip(),  
            'd': lines[4].split(') ')[1].strip()   
        }
        question_dict = {
            "question": question_text,
            "a": options['a'],
            "b": options['b'],
            "c": options['c'],
            "d": options['d'],
            "answer": answer_part[i]
        }
        quiz_list.append(question_dict)
    return quiz_list