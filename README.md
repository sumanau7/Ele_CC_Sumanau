Install dependencies in the project's lib directory.
   Note: App Engine can only import libraries from inside your project directory.

   ```
   git clone https://github.com/sumanau7/Ele_CC_Sumanau.git
   cd Ele_CC_Sumanau
   pip install -r requirements.txt -t lib
   ```
Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create a
   project/app id. (App id and project id are identical)
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   appcfg.py -A <your-project-id> --oauth2 update .
   ```
