from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts
posts = [
    {
        'title': 'Bridging the Digital Divide: How AI is Reshaping Access to Knowledge',
        'content': """In today’s world, artificial intelligence (AI) has transformed the way we access and share knowledge, but it’s also highlighting a pressing concern: the digital divide. The divide between those who have access to digital technology and those who do not has far-reaching effects, impacting education, employment, and economic opportunity. AI tools such as large language models, automated tutors, and knowledge-sharing platforms are powerful assets, but they’re largely available to populations with internet access, financial resources, and tech literacy.
        
As global economies work to integrate AI in meaningful ways, there is a call for policies that promote equitable access to technology. Public and private sectors must work collaboratively to make AI accessible and affordable while prioritizing digital literacy. Bridging this gap could democratize access to information, enable marginalized communities, and create opportunities that were previously out of reach.
        """,
        'author': 'Author One'
    },
    {
        'title': 'Remote Work Revolution: How Hybrid Models Are Redefining the Future of Work',
        'content': """The future of work is evolving, and hybrid work models have taken center stage. Companies worldwide are moving towards a blend of remote and in-office work arrangements, allowing for greater flexibility while maintaining collaboration. This shift isn’t just a trend but a significant redefinition of the workplace, with lasting implications for productivity, employee satisfaction, and talent acquisition.
        
The hybrid work model provides employees with autonomy and flexibility, which has been shown to improve job satisfaction and reduce burnout. Companies, on the other hand, gain access to a broader talent pool unrestricted by geographic boundaries. However, challenges remain, such as ensuring seamless communication, maintaining company culture, and handling cybersecurity concerns.
        """,
        'author': 'Author Two'
    },
    {
        'title': 'Sustainability in Tech: Green Computing and the Push for Eco-Friendly Practices',
        'content': """Sustainability in technology is more than just a buzzword; it’s a necessity. As digital technology advances, so does its environmental footprint, with data centers, cloud computing, and electronic waste contributing to pollution. This reality is pushing the tech industry to adopt sustainable practices that align with global eco-friendly goals. Green computing—using technology in a way that conserves energy and reduces e-waste—has emerged as a solution to minimize environmental impact.
        
Major companies are committing to carbon neutrality, optimizing their data centers, and adopting recyclable hardware designs. Additionally, practices such as server virtualization, energy-efficient algorithms, and eco-friendly coding are becoming mainstream. These initiatives represent a step toward a sustainable future, aligning innovation with environmental responsibility.
        """,
        'author': 'Author Three'
    }
]

@app.route('/')  # Route for home page
def home():
    return render_template('home.html')

@app.route('/blogs')  # Route for blog page
def blogs():
    return render_template('blogs.html', posts=posts)

@app.route('/contact')  # Route for contact page
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
