import mysql.connector
from werkzeug.utils import secure_filename

import os

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def configure_routes(app , mysql):
    from flask import render_template, request, redirect, url_for, session, flash, make_response
    from MySQLdb.cursors import DictCursor  
    from models import Registration  # ✅ safe now, no circular import


    # ---------- DB Connection ----------
    def get_db_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rachel_sql17",   # <-- your MySQL password
            database="faith_db"
        )

    # ---------- Public Routes ----------
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')
    
    @app.route('/plays')
    def plays():
        plays_data = [
            {
                "id": 1,
                "title": "JOSEPH(marathi)",
                "image": "/static/images/joseph.png",
                "description": "The Story OF Forgiveness."
            },
            {
                "id": 2,
                "title": "ESTHER",
                "image": "/static/images/esther.png",
                "description": "The Power & Providence Of God."
            },
            {
                "id": 3,
                "title": "THE NATIVITY",
                "image": "/static/images/nativity.png",
                "description": "The Birth Of Christ"
            },
             {
                "id": 4,
                "title": "DAVID",
                "image": "/static/images/david.png",
                "description": "The man After God's own heart."
            },
            {
                "id": 5,
                "title": "JOSEPH(English)",
                "image": "/static/images/josephe.png",
                "description": "The Story OF Forgiveness."
            },
             {
                "id": 6,
                "title": "SAMSON",
                "image": "/static/images/samson.png",
                "description": "The Protector Of Faith."
            },
             {
                "id": 7,
                "title": "MOSES",
                "image": "/static/images/moses.png",
                "description": "."
            },
            {
                "id": 8,
                "title": "JONAH",
                "image": "/static/images/jonah.png",
                "description": "God's Extreme Love For Mankind."
            },
            {
                "id": 9,
                "title": "RUTH",
                "image": "/static/images/ruth.png",
                "description": "The Women Of Faith."
            },
            {
                "id": 10,
                "title": "NOAH",
                "image": "/static/images/noah.png",
                "description": "."
            },
            {
                "id": 11,
                "title": "PASSION OF CHRIST",
                "image": "/static/images/poc.png",
                "description": "THE PASSION OF CHRIST."
            },


        ]
        return render_template("plays.html", plays=plays_data)


    @app.route('/plays/<int:play_id>')
    def play_detail(play_id):
        plays_data = {
            1: {
                "title": "JOSEPH(marathi)",
                "image": "/static/images/joseph.png",
                "description": "Joseph(Marathi) - The Story OF Forgiveness (2015).",
                "images": [
                    "/static/images/joseph1.png",
                    "/static/images/joseph2.png",
                    "/static/images/joseph3.png",
                    "/static/images/joseph4.png",
                    "/static/images/joseph5.png",
                    "/static/images/joseph6.png"
                    
                ],
                
            },
            2: {
                    "title": "ESTHER",
                    "image": "/static/images/esther.png",
                    "description": "Esther - The Power & Providence Of God (2024).",
                    "images": [
                        "/static/images/esther1.png",
                        "/static/images/esther2.png",
                        "/static/images/esther3.png",
                        "/static/images/esther4.png",
                        "/static/images/esther5.png",
                        "/static/images/esther6.png"
                    ],
                },

            3: {
                "title": "The Nativity",
                "image": "/static/images/nativity.png",
                "description": "The Nativity - The Birth Of Christ.(2021)",
                "images": [
                    "/static/images/nativity1.png",
                    "/static/images/nativity2.png",
                    "/static/images/nativity3.png",
                    "/static/images/nativity4.png",
                    "/static/images/nativity5.png",
                ],
                
            },
            4: {
                    "title": "DAVID",
                    "image": "/static/images/david.png",
                    "description": "David - The man After God's own heart (2023).",
                    "images": [
                        "/static/images/david1.png",
                        "/static/images/david2.png",
                        "/static/images/david3.png",
                        "/static/images/david4.png",
                        "/static/images/david5.png",
                        "/static/images/david6.png"
                    ],
                },
            5: {
                "title": "JOSEPH(English)",
                "image": "/static/images/josephe.png",
                "description": "Joseph - The Story OF Forgiveness (2022).",
                "images": [
                    "/static/images/josephe1.png",
                    "/static/images/josephe2.png",
                    "/static/images/josephe3.png",
                    "/static/images/josephe4.png",
                    "/static/images/josephe5.png",
                    "/static/images/josephe6.png"

                ],
                
            },
             9: {
                "title": "Ruth",
                "image": "/static/images/ruth.png",
                "description": "The Women Of Faith.(2018)",
                "images": [
                    "/static/images/ruth1.png",
                    "/static/images/ruth2.png",
                    "/static/images/ruth3.png",
                    "/static/images/ruth4.png",
                    "/static/images/ruth5.png",
                ],
                
            },
            8: {
                    "title": "JONAH",
                    "image": "/static/images/jonah.png",
                    "description": "Jonah - God's Extreme Love For Mankind.(2017).",
                    "images": [
                        "/static/images/jonah1.png",
                        "/static/images/jonah2.png",
                        "/static/images/jonah3.png",
                        "/static/images/jonah4.png",
                        "/static/images/jonah5.png",
                        "/static/images/jonah6.png"
                        
                    ],
                },
                7: {
                    "title": "MOSES",
                    "image": "/static/images/moses.png",
                    "description": "(2016).",
                    "images": [
                        "/static/images/moses1.png",
                        "/static/images/moses2.png",
                        "/static/images/moses3.png",
                        "/static/images/moses4.png",
                        "/static/images/moses5.png",
                        "/static/images/moses6.png"
                        
                        
                    ],
                },
                10: {
                    "title": "NOAH",
                    "image": "/static/images/noah.png",
                    "description": "(2014).",
                    "images": [
                        "/static/images/noah1.png",
                        "/static/images/noah2.png",
                        "/static/images/noah3.png",
                        "/static/images/noah4.png",
                        "/static/images/noah5.png",
                        "/static/images/noah6.png"
                        
                    ],
                },
                 6: {
                    "title": "SAMSON",
                    "image": "/static/images/samson.png",
                    "description": "(2014).",
                    "images": [
                        "/static/images/samson1.png",
                        "/static/images/samson2.png",
                        "/static/images/samson3.png",
                        "/static/images/samson4.png",
                        "/static/images/samson5.png",
                        "/static/images/samson6.png"
                        
                    ],
                },
                11: {
                    "title": "PASSION OF CHRIST",
                    "image": "/static/images/poc.png",
                    "description": "(2014).",
                    "images": [
                        "/static/images/poc1.png",
                        "/static/images/poc2.png",
                        "/static/images/poc3.png",
                        "/static/images/poc4.png",
                        "/static/images/poc5.png",
                        "/static/images/poc6.png"
                        
                    ],
                },
        }

        play = plays_data.get(play_id)
        if not play:
            return "Play not found", 404

        return render_template("play_detail.html", play=play)



   

# --- POC Form ---
    @app.route('/poc', methods=['GET', 'POST'])
    def poc():
        if request.method == 'POST':
            name = request.form['name']
            place = request.form['place']
            church = request.form['church']
            contact = request.form['contact']

            # ✅ insert into MySQL
            cursor = mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO poc_requests (name, place, church, contact) VALUES (%s, %s, %s, %s)",
                (name, place, church, contact)
            )
            mysql.connection.commit()
            cursor.close()

            flash("Your request has been submitted!", "success")
            return redirect(url_for('poc'))

        return render_template('poc.html')

    @app.route('/admin/poc')
    def admin_poc():
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))

        cursor = mysql.connection.cursor(DictCursor)
        cursor.execute("SELECT id, name, place, church, contact, created_at FROM poc_requests ORDER BY created_at DESC")
        requests = cursor.fetchall()
        cursor.close()

        return render_template('admin_poc.html', requests=requests)


    # ---------- Prayer Form ----------
    @app.route('/prayer', methods=['GET', 'POST'])
    def prayer():
        if request.method == 'POST':
            name = request.form.get('name')
            mobile = request.form.get('mobile')
            place = request.form.get('place')
            message = request.form.get('message')

            # Save to MySQL
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO prayers (name, mobile, place, message) VALUES (%s, %s, %s, %s)",
                (name, mobile, place, message)
            )
            conn.commit()
            cursor.close()
            conn.close()

            return render_template('prayer.html')
        return render_template('prayer.html')

    # ---------- Admin ----------
    @app.route('/admin/login', methods=['GET', 'POST'])
    def admin_login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if username == 'admin' and password == 'BrNana':
                session['admin_logged_in'] = True
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid username or password')
        return render_template('admin_login.html')

    @app.route('/admin')
    def admin_dashboard():
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return render_template('admin.html')

    @app.route('/admin/logout')
    def admin_logout():
        session.pop('admin_logged_in', None)
        return redirect(url_for('admin_login'))

    @app.route('/admin/prayers')
    def admin_prayers():
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))

        # Fetch from MySQL
        cursor = mysql.connection.cursor(DictCursor)
        cursor.execute("SELECT id, name, mobile, message, place, created_at FROM prayers")
        prayer_requests = cursor.fetchall()
        cursor.close()

        return render_template('admin_prayers.html', requests=prayer_requests)


# --- Public Events Page (Google Calendar + extra events from DB) ---
    @app.route('/events')
    def events():
         cursor = mysql.connection.cursor(DictCursor)
         cursor.execute("SELECT * FROM events")
         events = cursor.fetchall()
         cursor.close()
         return render_template("events.html", events=events)

# --- Event Detail + Registration Form ---
    @app.route('/events/<int:event_id>', methods=["GET", "POST"])
    def event_detail(event_id):
        cursor = mysql.connection.cursor(DictCursor)
        cursor.execute("SELECT * FROM events WHERE id = %s", (event_id,))
        event = cursor.fetchone()

        if not event:
            flash("Event not found!", "danger")
            return redirect(url_for('events'))

        if request.method == "POST":
            name = request.form['name']
            email = request.form['email']
            phone = request.form.get('phone')
            additional_info = request.form.get('additional_info')

            cursor.execute("""
                INSERT INTO event_registrations (event_id, name, email, phone, additional_info)
                VALUES (%s, %s, %s, %s, %s)
            """, (event_id, name, email, phone, additional_info))
            mysql.connection.commit()
            flash("You have successfully registered!", "success")
            return redirect(url_for('event_detail', event_id=event_id))

        cursor.execute("SELECT * FROM event_registrations WHERE event_id = %s", (event_id,))
        registrations = cursor.fetchall()
        cursor.close()

        return render_template("event_detail.html", event=event, registrations=registrations)

# --- Admin: Manage Events ---
    @app.route('/admin/events' , endpoint='admin_events')
    def admin_events():
        cursor = mysql.connection.cursor(DictCursor)
        cursor.execute("SELECT * FROM events")
        events = cursor.fetchall()
        cursor.close()
        return render_template("admin_events.html", events=events)

    @app.route('/admin/events/add', methods=["POST"])
    def add_event():
        title = request.form['title']
        date = request.form['date']
        description = request.form['description']
        form_link = request.form.get('form_link')
        has_registration = 1 if request.form.get('has_registration') else 0

        file = request.files.get('image')
        image_path = None

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename).lower()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = filename  # ✅ save filename only; no 'event' object needed



        cursor = mysql.connection.cursor()
        cursor.execute("""
        INSERT INTO events (title, date, description, form_link, has_registration, image_path)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (title, date, description, form_link, has_registration, image_path))
        mysql.connection.commit()
        cursor.close()

        flash("Event added successfully!", "success")
        return redirect(url_for('admin_events'))

    @app.route('/admin/events/delete/<int:event_id>')
    def delete_event(event_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
        mysql.connection.commit()
        cursor.close()
        flash("Event deleted!", "danger")
        return redirect(url_for('admin_events'))
    
    @app.route("/admin/registrations")
    def admin_registrations():
        cursor = mysql.connection.cursor(DictCursor)  # ✅ get cursor

        query = """
        SELECT e.id AS event_id, e.title AS event, e.date, r.name, r.email, r.phone, r.additional_info
        FROM event_registrations r
        JOIN events e ON r.event_id = e.id
        ORDER BY e.date DESC
    """
        cursor.execute(query)
        registrations = cursor.fetchall()
        cursor.close()

        return render_template("admin_registrations.html", registrations=registrations)


    @app.route("/admin/registrations/download")
    def download_registrations():
        # Get event_id from query string (?event_id=1)
        event_id = request.args.get("event_id", type=int)
        if not event_id:
            return "event_id is required", 400

        cursor = mysql.connection.cursor(DictCursor)
        query = """
            SELECT e.title, e.date, r.name, r.email, r.phone, r.additional_info
            FROM event_registrations r
            JOIN events e ON r.event_id = e.id
            WHERE e.id = %s
            ORDER BY e.date DESC
        """
        cursor.execute(query, (event_id,))
        registrations = cursor.fetchall()
        cursor.close()

        # Build CSV rows
        csv_rows = []
        header = ["Event", "Date", "Name", "Email", "Phone", "Info"]
        csv_rows.append(header)

        for row in registrations:
            csv_rows.append([
                row["title"],
                row["date"],
                row["name"],
                row["email"],
                row["phone"],
                row["additional_info"]
            ])

        # Convert to CSV string
        csv_string = "\n".join([",".join(map(str, r)) for r in csv_rows])

        # Stream as CSV response
        response = make_response(csv_string)
        response.headers["Content-Disposition"] = "attachment; filename=registrations.csv"
        response.headers["Content-Type"] = "text/csv"
        return response

