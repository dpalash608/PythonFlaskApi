import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyBlZvQYgaofBGUaj4OBdFEXaRFyYHuhdJQ"

import google.generativeai as genai
import evaluate

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("summarize this html content in paragraph '<HTML><BODY><p><span id='cke_bm_11058S' "
                                  "style='display:none'>&nbsp;</span>&nbsp;</p> <p>&nbsp;</p> <p><img alt='Image' "
                                  "src='https://performancemanager5.successfactors.eu/public/ui-resource/SAP/263;mod"
                                  "=6912a54fa9243908d07e448274529154&amp;resize=wlx' style='height:36px; width:150px' "
                                  "/><br /> </p> <table border='1' cellpadding='1' cellspacing='1' "
                                  "style='width:100%'> <tbody> <tr> <td>Absence duration</td> <td>Time Type</td> "
                                  "<td>Number of Days</td> <td>Calendar Days</td> </tr> <tr> "
                                  "<td>02/05/2024&nbsp;-&nbsp;02/06/2024</td> <td>Vacation</td> <td>2</td> <td>2</td> "
                                  "</tr><tr> <td>02/12/2024&nbsp;-&nbsp;02/12/2024</td> <td>Maternity</td> <td>1</td> "
                                  "<td>1</td> </tr><tr> <td>02/13/2024&nbsp;-&nbsp;02/13/2024</td> <td>Vacation</td> "
                                  "<td>1</td> <td>1</td> </tr><tr> <td>02/14/2024&nbsp;-&nbsp;02/14/2024</td> <td>IRL "
                                  "Adoption Leave – Paid</td> <td>1</td> <td>1</td> </tr><tr> "
                                  "<td>02/20/2024&nbsp;-&nbsp;02/20/2024</td> <td>IRL Adoption Leave – Paid</td> "
                                  "<td>1</td> <td>1</td> </tr> </tbody> </table> <p>Total absence in calendar days "
                                  ":-6</p> <p>Total absence :-6</p> <p><span id='cke_bm_1946S' "
                                  "style='display:none'>&nbsp;</span></p> </BODY></HTML>'")
print(response.text)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
response = model.generate_content("convert this in hindi" + " " + response.text)
print(response.text)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

rouge = evaluate.load('rouge')
candidates = ["Summarization is cool", "I love Machine Learning", "Good night"]

references = [["Summarization is beneficial and cool", "Summarization saves time"],
              ["People are getting used to Machine Learning", "I think i love Machine Learning"],
              ["Good night everyone!", "Night!"]
                ]
results = rouge.compute(predictions=candidates, references=references)
print(results)
