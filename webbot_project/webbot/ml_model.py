# webbot/ml_model.py

import wolframalpha
import wikipedia


def predict(query):
    try:
        # Connect to WolframAlpha API
        client = wolframalpha.Client("972AR5-4P7L97GLGJ")

        # Query WolframAlpha for the result
        res = client.query(query)
        ans = next(res.results).text

        return ans

    except Exception as e:
        print(f"WolframAlpha error: {e}")

        try:
            # Query Wikipedia for the summary
            ans = wikipedia.summary(query, sentences=3)

            return ans

        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Wikipedia disambiguation error: {e}")
            options = e.options[:5]  # Show up to 5 options
            return f"Wikipedia may refer to: {', '.join(options)}"

        except wikipedia.exceptions.PageError as e:
            print(f"Wikipedia page error: {e}")
            return "No information found in Wikipedia."

        except Exception as e:
            print(f"Other Wikipedia error: {e}")
            return "Error fetching data."
