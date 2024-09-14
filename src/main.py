if __name__ == "__main__":
    # Step 1: Load profile and followers
    profile_name = "PUBLIC_ACCOUNT_NAME"
    instagram_loader = InstagramDataLoader(profile_name)
    profile = instagram_loader.load_profile()
    followers = instagram_loader.get_followers(profile)

    # Step 2: Initialize BioAnalyzer and LinkFilter
    bio_analyzer = BioAnalyzer()
    link_filter = LinkFilter(bio_analyzer)

    # Step 3: Filter users with links
    users_with_links = link_filter.filter_users_with_links(followers)

    # Step 4: Store users with links in UserManager and print them
    user_manager = UserManager()
    for user, bio in users_with_links:
        user_manager.add_user(user, bio)

    # Step 5: Output results
    user_manager.print_users()
