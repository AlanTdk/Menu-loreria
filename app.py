from flask import Flask, render_template
import urllib.parse

# Initialize the Flask application
app = Flask(__name__)

# Main route that renders the flower shop's digital menu
@app.route('/')
def menu():
    """
    Renders the main page for the Ramos Alba digital menu.
    """
    # Shop information
    shop_info = {
        "name": "Ramos Alba",
        "slogan": "¡Me encantaría hacer tu próximo envío de flores!",
        "whatsapp_number": "5219613782935",  # Número con código de país 52 + 1
        "display_phone": "961 378 2935",
        "instagram_url": "https://www.instagram.com/ramos_albaaa/",
        "tiktok_url": "https://www.tiktok.com/@ramos_alba"
    }
    
    # Generate WhatsApp link for quotes
    quote_message = "Hola, me gustaría cotizar un ramo de flores personalizado. 💐"
    shop_info['whatsapp_quote_url'] = f"https://wa.me/{shop_info['whatsapp_number']}?text={urllib.parse.quote(quote_message)}"

    # Gallery of bouquets
    bouquets = [
        {"name": "Sonrojo Primaveral", "image": "images/ramo1.jpg", "description": "Una delicada mezcla de rosas y gerberas en tonos pastel."},
        {"name": "Elegancia Blanca", "image": "images/ramo2.jpg", "description": "Un clásico atemporal con liliums y nardos blancos puros."},
        {"name": "Atardecer Tropical", "image": "images/ramo3.jpg", "description": "Explosión de colores con aves del paraíso y flores exóticas."},
        {"name": "Abrazo de Girasoles", "image": "images/ramo4.jpg", "description": "Para iluminar el día de cualquiera con la alegría de los girasoles."},
        {"name": "Sueño de Lavanda", "image": "images/ramo5.jpg", "description": "Relajante y aromático, con lavanda fresca y lisianthus morados."},
        {"name": "Corazón Intenso", "image": "images/ramo6.jpg", "description": "La máxima expresión de amor con 50 rosas rojas premium."},
        {"name": "Jardín Secreto", "image": "images/ramo7.jpg", "description": "Un arreglo silvestre y orgánico con flores de temporada."},
        {"name": "Cielo Azul", "image": "images/ramo8.jpg", "description": "Un sereno ramo con hortensias azules y delphinium."},
        {"name": "Fuego y Pasión", "image": "images/ramo9.jpg", "description": "Una combinación vibrante de tulipanes rojos y naranjas."},
        {"name": "Dulce Aniversario", "image": "images/ramo10.jpg", "description": "Perfecto para celebrar, con flores surtidas y follaje fino."}
    ]

    # Special promotions
    promotions = [
        {
            "title": "Ramo del Mes con 15% OFF",
            "description": "Cada mes seleccionamos una combinación única de flores de temporada a un precio especial. ¡Pregunta por el ramo de este mes y sorpréndete!",
            "image": "images/promocion.jpg"
        }
    ]

    return render_template('index.html', info=shop_info, bouquets=bouquets, promotions=promotions)

# Allows running the app directly
if __name__ == '__main__':
    # Ensure you are using python3 to run if you encounter issues
    app.run(debug=True)
