from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulating a database with lists (for simplicity)
users = []
posts = []

# Home page
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.append({'username': username, 'password': password})
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        if user:
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template('login.html')

# Create a new post
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        flash('Post created successfully!')
        return redirect(url_for('index'))
    return render_template('create_post.html')

# Edit a post
@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = posts[post_id]
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        flash('Post updated successfully!')
        return redirect(url_for('index'))
    return render_template('edit_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
