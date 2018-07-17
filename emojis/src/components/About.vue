<template>
	<div class="about">
		<h1> Hello {{ some_name}}This is an about page</h1>
		<p>About</p>
		
	</div>
</template>

<script type="text/javascript">
	export default{
		name: 'Skills',
		data() {
			return {
				some_name: this.$route.params.name 
			}
		}
	}
</script>
