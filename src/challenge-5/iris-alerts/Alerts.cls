Class CoffeeCo.Alerts Extends %Persistent
{

Property AlertId As %Integer;

Property ProductId As %Integer;

Property AlertType As %String;

Property CreatedAt As %TimeStamp;

/// Save an alert to database
ClassMethod SaveAlert(pProductId As %Integer, pAlertType As %String) As %Status
{
        Set sc = $$$OK
        
        set alert = ##class(CoffeeCo.Alerts).%New()
        set alert.ProductId = pProductId
        set alert.AlertType = pAlertType
        set alert.CreatedAt = $ZDATETIME($HOROLOG, 3)
        set sc = alert.%Save()

        quit sc
}

/// Send Out Of Stock Alert
ClassMethod SendOutOfStockAlert(pProductId As %Integer, pName As %String) As %String [ Language = python ]
{
        from email.mime.text import MIMEText
        import smtplib
        import iris

        msg = MIMEText(f"OUT OF STOCK ALERT! {pProductId} is out of stock.")
        msg['Subject'] = f'{pProductId} Out of Stock'
        msg['From'] = "CoffeeCo Inventory Alerts <alerts@coffeeco.com>"
        msg['To'] = "inventory_manager@coffeeco.com"

        # Send the email
        ## with smtplib.SMTP('localhost') as server:
            ## server.send_message(msg)

        iris.CoffeeCo.Alerts.SaveAlert(pProductId, "OutOfStock")
        line = 40*"="
        response = line + "\n" + f"Out of stock alert sent for ProductID: {pProductId}, ProductName: {pName}" + "\n" + line
        return response
}

}
