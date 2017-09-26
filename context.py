class Context(object):
	
	def __init__(self):
		self._function_name = "context-sample"
		self._function_version = "$LATEST"
		self._invoked_function_arn = "arn:aws:lambda:ap-northeast-1:XXXXXXXXXX:function:context-sample"
		self._memory_limit_in_mb = 128
		self._aws_request_id = "3758b2ae-1448-11e7-beb3-a31cd530126e"
		self._log_group_name = "/aws/lambda/context-sample"
		self._log_stream_name = "2017/01/01/[$LATEST]e9b90e266ea54d88b804beb73521b45c"

	@property
	def function_name(self):
		return self._function_name

	@property
	def function_version(self):
		return self._function_version

	@property
	def invoked_function_arn(self):
		return self._invoked_function_arn

	@property
	def memory_limit_in_mb(self):
		return self._memory_limit_in_mb

	@property
	def aws_request_id(self):
		return self._aws_request_id

	@property
	def log_group_name(self):
		return self._log_group_name

	@property
	def log_stream_name(self):
		return self._log_stream_name

if __name__ == "__main__":
	context = Context()
	print(context.function_name)
	print(context.log_group_name)
