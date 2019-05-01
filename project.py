import re
import zlib
import cv2

from scapy.all import *

pictures_directory = "/home/tyler/scripts/pictures"
faces_directory = "/home/tyler/scripts/faces"
pcap_file = "/home/tyler/scripts/images5.pcap"

def get_http_headers(http_payload):
	try:
		headers_raw = http_payload[:http_payload.index("\r\n\r\n")+2]
		headers = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", headers_raw))
	except:
		return None
	if "Content-Type" not in headers:
		return none
	return headers

#She makes it this far
def extract_image(headers,http_payload):
	
	image = None
	image_type = None
	
	try:
		if "image" in headers['Content-Type']:
		
			image_type = headers['Content-Type'].split("/")[1]
			
			image = http_payload[http_payload.index("\r\n\r\n")+4:]

			try:
				if "Content-Encoding" in headers.keys():
					if headers['Content-Encoding'] == "gzip":
						image = zlib.decompress(image, 16+zlib.MAX_WBITS)
					elif headers['Content-Encoding'] == "deflate":
						image = zlib.decompress(image)
			except Exception as e:
				print(e)
	except:
			return None,None

	return image,image_type

#She makes it this far


def face_detect(path, file_name):
	
	img = cv2.imread(path)
	cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
	rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
		
	if len(rects) == 0:
		return False
	rects[:, 2:] += rects[:, :2]

	for x1,y1,x2,y2 in rects:
		cv2.rectangle(img,(x1,y1),(x2,y2),(127,255,0),2)
	cv2.imwrite("%s/%s-%s" % (faces_directory,pcap_file,file_name),img)
	return True

	

#She makes it this far

def http_assembler(pcap_file):
	
	carved_images = 0
	faces_detected = 0
	
	a = rdpcap(pcap_file)
	sessions = a.sessions()

	for session in sessions:
		http_payload = b""
		for packet in sessions[session]:
			#code is not reached
			try:
				if packet[TCP].dport == 80 or packet[TCP].sport == 80:
					
					http_payload += bytes(packet[TCP].payload)
			except Exception as e:
				print(e)
		headers = dict(re.findall(b"((?P<name>.*?): (?P<value>.*?)\r\n", headers_raw))

		if headers is None:
			continue
			#code is not reached
		image,image_type = extract_image(headers,http_payload)

		if image is not None and image_type is not None:
		
			file_name = "%s-pic_carver_%d.%s" % (pcap_file,carved_images,image_type)
			#Code is not reached here
			fd = open("%s/%s" % (pictures_directory,file_name),"wb")
			
			fd.write(image)
			fd.close()
			
			carved_images += 1
			
			try:
				result = face_detect("%s/%s" % (pictures_directory,file_name),file_name)
				
				if result is True:
					faces_detected += 1
					#Code is not reached here
			except Exception as e:
				print(e)
				
			
			return carved_images, faces_detected
	
		carved_images, faces_detected = http_assembler(pcap_file)
	
		print ("Extracted: %d images" % carved_images)
		print ("Detected: %d faces" % faces_detected)
		print("hi")  #This is a test to see if the code reaches this point
