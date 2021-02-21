# viam
Viam is an auto mindmapper designed with simplicity in mind.
Viam script features :
```
-- Comment: any line starts with -- symbols is a comment and will be ignored. Note that there is no inline comment.
-- Metadata: any line starts with + symbol is a metadata line used to customize the mindmap property
-- Subnode are specify with tab (as in \t not space); note that the root node (i.e. the topic node) should not contain any tab.
-- Modifier line: any line starts with with % symbol will modify the line immediately below it.
	-- Each attributes are separated with ;
-- Example:

+ font : Noto Sans Thai
+ size : 12

-- This is the mindmap about air
% size : 16
Air
	Oxygen
		About 22%
		Important to life
	Nitrogen
		About 75%
		Metabolically innert.
	Carbon Dioxide
		Bad stuff
			Global warming
			Waste produced in the body
		Less than 1%
```
