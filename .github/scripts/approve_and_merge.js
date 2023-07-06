module.exports = async ({ github, context }) => {
    console.log("this is context:\n  %s", context)
    console.log("\n\nthis is github:\n  %s", github)
}