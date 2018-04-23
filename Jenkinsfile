node{
    def gitUrl = 'https://api.github.com/repos/ManikyaVinay/PRB/commits'

    // Reading projects from GitLab REST API
    def projectURL = new URL("${gitUrl}")
    def commits = new groovy.json.JsonSlurper().parse(projectURL.newReader())
    def lastcommitid = "${commits[0].sha}"
    println lastcommitid
    def someothercommitid = "abcd"
    def lastcommit = ""
    if( ("abcd" != someothercommitid) || !lastcommit?.trim() ) {
        echo "commits are  different, so should call shared process lib"
    }
    else{
        echo "no need of shared process lib as lastcommit is not empty or commits are same"
    }
}
