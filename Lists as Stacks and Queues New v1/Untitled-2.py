
pki csr cms1 CN:hq-cms1.ccie.collabcert.com subjectAltName:hq-cms2.ccie.collabcert.com,hq-cms3.ccie.collabcert.com,join.ccie.collabcert.com,ccie.collabcert.com

pki csr dbserver CN:hq-cms1.ccie.collabcert.com subjectAltName:hq-cms2.ccie.collabcert.com,hq-cms3.ccie.collabcert.com

pki csr dbclient CN:postgrest


database cluster dbserver.key dbserver.cer dbclient.key dbclient.cer rootca.cer
database cluster localnode a
database cluster initialize / join 192.100.64.31
database cluster status

webadmin certs cms1.key cms1.cer rootca.cer
webadmin listen a 8443
webadmin enable

callbridge certs cms1.key cms1.cer rootca.cer
callbridge listen a 
callbridge enable