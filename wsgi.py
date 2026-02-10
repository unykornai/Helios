"""
☀ HELIOS — Production WSGI Entry Point
═══════════════════════════════════════
Use this with a production WSGI server:

  waitress-serve --host=0.0.0.0 --port=5050 wsgi:application
  gunicorn -w 4 -b 0.0.0.0:5050 wsgi:application

Never use `python app.py` in production.
"""

from app import create_app

application = create_app()

if __name__ == "__main__":
    # Fallback: python wsgi.py still works but uses waitress if available
    try:
        from waitress import serve
        print("☀ HELIOS — Production server (waitress)")
        serve(application, host="0.0.0.0", port=5050, threads=8)
    except ImportError:
        print("☀ HELIOS — Dev server (install waitress for production)")
        application.run(host="0.0.0.0", port=5050, debug=False)
