from flask import Flask,render_template,request
from campus_graph import shortest_route,locations
import folium

app = Flask(__name__)

users = {

"22B81A0501":"pass123"

}

@app.route("/")
def login():

    return render_template(
        "login.html"
    )


@app.route("/home",methods=["POST"])
def home():

    roll=request.form["roll"]

    password=request.form["password"]

    if roll in users and users[roll]==password:

        return render_template(
            "home.html"
        )

    return "Invalid Login"


@app.route("/route",methods=["POST"])
def route():

    start=request.form["start"]

    end=request.form["destination"]

    path=shortest_route(
        start,
        end
    )

    coords=[]

    for p in path:

        coords.append(
            locations[p]
        )

    m = folium.Map(

        location=coords[0],

        zoom_start=18
    )

    folium.PolyLine(

        coords,

        weight=8

    ).add_to(m)

    for point in path:

        folium.Marker(

            locations[point],

            popup=point

        ).add_to(m)

    map_html = m._repr_html_()

    return render_template(

        "route.html",

        map_html=map_html,

        path=path
    )


if __name__=="__main__":

    app.run(debug=True)