from flask import Flask, jsonify, request
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Function to create a connection to the PostgreSQL database
def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="wkypzjoe",
            user="wkypzjoe",
            password="cHrM4DgWRv4ObnTXF24uMWTXH0UH4mKw",
            host="berry.db.elephantsql.com",
            port="5432"
        )
    except psycopg2.Error as e:
        print(e)
    return conn

# Route to fetch global job listings
@app.route('/job_listings', methods=['GET'])
def get_job_listings():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM talentsync.job")
            data = cursor.fetchall()
            conn.close()
            return jsonify({'job_listings': data}), 200
        except psycopg2.Error as e:
            conn.rollback()
            conn.close()
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Unable to connect to the database'}), 500

# Route to fetch feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM talentsync.feedback")
            data = cursor.fetchall()
            conn.close()
            return jsonify({'feedback': data}), 200
        except psycopg2.Error as e:
            conn.rollback()
            conn.close()
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Unable to connect to the database'}), 500


# Route to add feedback
@app.route('/add_feedback', methods=['POST'])
def add_feedback():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            data = request.get_json()
            feedback_type = data.get('feedback_type')
            message = data.get('message')
            job_id = data.get('job_id')  # Assuming feedback is related to a job
            rating = data.get('rating')
            user_id = data.get('user_id')
            employer_id = data.get('employer_id')

            # Insert feedback into the 'feedback' table
            insert_query = sql.SQL("INSERT INTO talentsync.feedback (feedback_type, message, job_id, rating, user_id, employer_id) VALUES (%s, %s, %s, %s, %s, %s)")
            cursor.execute(insert_query, (feedback_type, message,int(job_id) if job_id else None, int(rating) if rating else None, int(user_id) if user_id else None, int(employer_id) if employer_id else None))
            
            conn.commit()
            conn.close()
            return jsonify({'message': 'Feedback added successfully'}), 200
        except (psycopg2.Error, KeyError) as e:
            conn.rollback()
            conn.close()
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Unable to connect to the database'}), 500

if __name__ == '__main__':
    app.run(debug=True)
