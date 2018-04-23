node{
    def gitUrl = 'https://api.github.com/repos/ManikyaVinay/PRB/commits'

    // Reading projects from GitLab REST API
    def projectList = new URL("${gitUrl}")
    def projects = new groovy.json.JsonSlurper().parse(projectList.newReader())
    def lastcommitid = ${projects[0].sha}
    println lastcommitid
    projects.each {
      println it.sha
    }
}
