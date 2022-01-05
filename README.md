# Marc in da house

Before changing the visibility of this repo consider undoing the following diff:

```
diff --git a/web/actions.html b/web/actions.html
index 8970c78..928220c 100644
--- a/web/actions.html
+++ b/web/actions.html
@@ -10,7 +10,8 @@
     <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
     <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
     <script>
-    var host = prompt('Enter the host:port of the controls API')
+    var host = 'http://188.84.150.239:1505';
+    // var host = prompt('Enter the host:port of the controls API')
     function setAction(action) {
         $.ajax({
             url: host + '/action',
diff --git a/web/colors.html b/web/colors.html
index 5d56dfc..dc7cfd5 100644
--- a/web/colors.html
+++ b/web/colors.html
@@ -16,7 +16,8 @@
             'left': 'green',
             'right': 'yellow',
         };
-        var host = prompt('Enter the host:port of the controls API')
+        var host = 'http://192.168.0.13:1505';
+        // var host = prompt('Enter the host:port of the controls API')
         setInterval(
             function() {
                 $.ajax({
```
