from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Python!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




import subprocess
import pkg_resources
import os

def run_script(script_name):
    script_path = pkg_resources.resource_filename('your_module', f'scripts/{script_name}')
    if os.path.exists(script_path):
        subprocess.run([script_path], check=True)
    else:
        raise FileNotFoundError(f"Script {script_name} not found!")

# Example usage:
run_script('script1.sh')






from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/file', methods=['POST', 'DELETE'])
def handle_file_request():
    file_path = request.args.get('path')
    if not file_path:
        return jsonify({'error': 'Path parameter is missing'}), 400

    if request.method == 'POST':
        # Create the file
        try:
            with open(file_path, 'w'):
                pass  # Empty file
            return jsonify({'message': f'File created at {file_path}'}), 201
        except Exception as e:
            return jsonify({'error': f'Failed to create file: {str(e)}'}), 500

    elif request.method == 'DELETE':
        # Delete the file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return jsonify({'message': f'File deleted at {file_path}'}), 200
            else:
                return jsonify({'error': 'File does not exist'}), 404
        except Exception as e:
            return jsonify({'error': f'Failed to delete file: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
